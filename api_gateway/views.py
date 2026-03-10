import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


@api_view(['GET'])
def books_api(request):
    r = requests.get("http://book-service:8000/books/")
    return Response(r.json())


@api_view(['PUT'])
def update_cart_item(request, item_id):
    # Forward to cart service
    try:
        r = requests.put(f"http://cart-service:8000/cart/item/{item_id}/", json=request.data)
        return Response(r.json(), status=r.status_code)
    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(['DELETE'])
def delete_cart_item(request, item_id):
    # Forward to cart service
    try:
        r = requests.delete(f"http://cart-service:8000/cart/item/{item_id}/delete/")
        return Response(r.json() if r.content else {"message": "Deleted"}, status=r.status_code)
    except Exception as e:
        return Response({"error": str(e)}, status=500)


def books(request):
    try:
        r = requests.get("http://book-service:8000/books/", timeout=5)
        if r.status_code == 200:
            books = r.json()
        else:
            books = []
    except requests.exceptions.RequestException as e:
        books = []
        print(f"Error fetching books: {e}")
    return render(request, 'books.html', {
        'books': books,
        'user_name': request.session.get('user_name'),
        'user_id': request.session.get('user_id')
    })


def book_detail(request, book_id):
    try:
        r = requests.get(f"http://book-service:8000/books/{book_id}/")
        if r.status_code == 200:
            book = r.json()
        else:
            book = None
    except requests.exceptions.RequestException as e:
        book = None
        print(f"Error fetching book {book_id}: {e}")
    
    if not book:
        return render(request, 'book_detail.html', {
            'error': 'Sách không tồn tại',
            'user_name': request.session.get('user_name'),
            'user_id': request.session.get('user_id')
        })
    
    return render(request, 'book_detail.html', {
        'book': book,
        'user_name': request.session.get('user_name'),
        'user_id': request.session.get('user_id')
    })


def register_customer(request):
    if request.method == 'POST':
        data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'password': request.POST['password'],
        }
        r = requests.post("http://customer-service:8000/customers/", json=data)
        if r.status_code in [200, 201]:
            return HttpResponseRedirect(reverse('books'))
        else:
            return render(request, 'register.html', {
                'error': 'Registration failed',
                'user_name': request.session.get('user_name'),
                'user_id': request.session.get('user_id')
            })
    return render(request, 'register.html', {
        'user_name': request.session.get('user_name'),
        'user_id': request.session.get('user_id')
    })


def login_customer(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        # Check credentials with customer service
        try:
            r = requests.get(f"http://customer-service:8000/customers/check/?email={email}&password={password}")
            if r.status_code == 200:
                customer_data = r.json()
                # Store user info in session
                request.session['user_id'] = customer_data['id']
                request.session['user_name'] = customer_data['name']
                request.session['user_email'] = customer_data['email']
                messages.success(request, f'Chào mừng {customer_data["name"]}!')
                return HttpResponseRedirect(reverse('books'))
            else:
                messages.error(request, 'Email hoặc mật khẩu không đúng!')
        except Exception as e:
            messages.error(request, 'Lỗi kết nối. Vui lòng thử lại!')
    
    return render(request, 'login.html', {
        'user_name': request.session.get('user_name'),
        'user_id': request.session.get('user_id')
    })


def logout_customer(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        del request.session['user_name']
        del request.session['user_email']
    messages.info(request, 'Đã đăng xuất!')
    return HttpResponseRedirect(reverse('books'))


def manage_books(request):
    try:
        r = requests.get("http://book-service:8000/books/")
        if r.status_code == 200:
            books = r.json()
        else:
            books = []
    except Exception as e:
        books = []
        print(f"Error fetching books in manage_books: {e}")
    return render(request, 'manage_books.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        data = {
            'title': request.POST['title'],
            'author': request.POST['author'],
            'price': request.POST['price'],
            'description': request.POST['description'],
            'stock': request.POST['stock'],
        }
        try:
            r = requests.post("http://book-service:8000/books/", json=data)
            print(f"Add book response status: {r.status_code}")
            print(f"Add book response text: {r.text}")
            print(f"Add book response headers: {r.headers}")
            if r.status_code in [200, 201]:
                try:
                    resp_data = r.json()
                    print(f"Add book response JSON: {resp_data}")
                    return HttpResponseRedirect(reverse('manage_books'))
                except Exception as e:
                    print(f"Error parsing JSON: {e}")
                    return render(request, 'add_book.html', {'error': f'Failed to parse response: {e}'})
            else:
                return render(request, 'add_book.html', {'error': f'Failed to add book: {r.status_code}'})
        except Exception as e:
            print(f"Exception in add_book: {e}")
            return render(request, 'add_book.html', {'error': f'Error: {str(e)}'})
    return render(request, 'add_book.html')


def edit_book(request, book_id):
    if request.method == 'POST':
        data = {
            'title': request.POST['title'],
            'author': request.POST['author'],
            'price': request.POST['price'],
            'description': request.POST['description'],
            'stock': request.POST['stock'],
        }
        r = requests.put(f"http://book-service:8000/books/{book_id}/", json=data)
        if r.status_code in [200, 201]:
            return HttpResponseRedirect(reverse('manage_books'))
        else:
            return render(request, 'edit_book.html', {'error': 'Failed to update book', 'book': data})
    else:
        try:
            r = requests.get(f"http://book-service:8000/books/{book_id}/")
            if r.status_code == 200:
                book = r.json()
                return render(request, 'edit_book.html', {'book': book})
            else:
                return render(request, 'edit_book.html', {'error': 'Book not found'})
        except Exception as e:
            return render(request, 'edit_book.html', {'error': 'Error fetching book'})


def delete_book(request, book_id):
    try:
        r = requests.delete(f"http://book-service:8000/books/{book_id}/")
        if r.status_code not in [200, 204]:
            print(f"Failed to delete book: status {r.status_code}")
    except Exception as e:
        print(f"Error deleting book: {e}")
    return HttpResponseRedirect(reverse('manage_books'))


def view_cart(request, customer_id):
    # Check if user is logged in
    if 'user_id' not in request.session:
        messages.warning(request, 'Vui lòng đăng nhập để xem giỏ hàng!')
        return HttpResponseRedirect(reverse('login'))
    
    # Check if user is trying to access their own cart
    if request.session['user_id'] != customer_id:
        messages.error(request, 'Bạn không có quyền xem giỏ hàng này!')
        return HttpResponseRedirect(reverse('books'))
    
    r = requests.get(f"http://cart-service:8000/cart/{customer_id}/")
    if r.status_code == 200:
        cart_items = r.json()
        
        # Enrich cart items with book information
        enriched_items = []
        total_amount = 0
        for item in cart_items:
            try:
                book_r = requests.get(f"http://book-service:8000/books/{item['book_id']}/")
                if book_r.status_code == 200:
                    book = book_r.json()
                    item_total = book['price'] * item['quantity']
                    enriched_item = {
                        'id': item['id'],
                        'book': book,
                        'quantity': item['quantity'],
                        'item_total': item_total
                    }
                    enriched_items.append(enriched_item)
                    total_amount += item_total
            except Exception as e:
                print(f"Error fetching book {item['book_id']}: {e}")
        
        items = enriched_items
    else:
        items = []
        total_amount = 0
    
    return render(request, 'cart.html', {
        'cart_items': items,
        'total_amount': total_amount,
        'user_name': request.session.get('user_name'),
        'user_id': request.session.get('user_id')
    })


def add_to_cart(request, book_id):
    # Check if user is logged in
    if 'user_id' not in request.session:
        messages.warning(request, 'Vui lòng đăng nhập để thêm sách vào giỏ hàng!')
        return HttpResponseRedirect(reverse('login'))
    
    # Add to cart service
    data = {
        'book_id': book_id,
        'customer_id': request.session['user_id'],
        'quantity': 1
    }
    
    try:
        r = requests.post("http://cart-service:8000/cart/add/", json=data)
        if r.status_code in [200, 201]:
            messages.success(request, 'Sách đã được thêm vào giỏ hàng!')
        else:
            messages.error(request, f'Lỗi khi thêm vào giỏ hàng: {r.status_code}')
    except Exception as e:
        messages.error(request, f'Lỗi kết nối: {str(e)}')
    
    return HttpResponseRedirect(reverse('books'))


def checkout(request):
    # Check if user is logged in
    if 'user_id' not in request.session:
        messages.warning(request, 'Vui lòng đăng nhập để thanh toán!')
        return HttpResponseRedirect(reverse('login'))
    
    customer_id = request.session['user_id']
    
    # Get cart items from cart service
    r = requests.get(f"http://cart-service:8000/cart/{customer_id}/")
    if r.status_code == 200:
        cart_items = r.json()
        
        # Enrich cart items with book information
        enriched_items = []
        total_amount = 0
        for item in cart_items:
            try:
                book_r = requests.get(f"http://book-service:8000/books/{item['book_id']}/")
                if book_r.status_code == 200:
                    book = book_r.json()
                    item_total = book['price'] * item['quantity']
                    enriched_item = {
                        'id': item['id'],
                        'book': book,
                        'quantity': item['quantity'],
                        'item_total': item_total
                    }
                    enriched_items.append(enriched_item)
                    total_amount += item_total
            except Exception as e:
                print(f"Error fetching book {item['book_id']}: {e}")
        
        if not enriched_items:
            messages.warning(request, 'Giỏ hàng trống!')
            return HttpResponseRedirect(reverse('books'))
        
        if request.method == 'POST':
            # Get customer info from session
            customer_name = request.session.get('user_name', 'Khách hàng')
            customer_email = request.session.get('user_email', 'guest@example.com')
            address = request.POST['address']
            
            # Create order data
            order_data = {
                'customer_id': customer_id,
                'customer_name': customer_name,
                'customer_email': customer_email,
                'address': address,
                'items': enriched_items,
                'total_amount': total_amount
            }
            
            # For demo, just clear cart and show success
            # In real app, would call order service
            try:
                clear_r = requests.delete(f"http://cart-service:8000/cart/{customer_id}/clear/")
            except:
                pass  # Ignore if clear endpoint doesn't exist
            
            messages.success(request, 'Đặt hàng thành công!')
            return render(request, 'order_success.html', {
                'order': {'id': 'DEMO-001', 'total': total_amount}
            })
        
        return render(request, 'checkout.html', {
            'cart_items': enriched_items,
            'total_amount': total_amount,
            'user_name': request.session.get('user_name'),
            'user_id': request.session.get('user_id')
        })
    
    else:
        messages.warning(request, 'Không thể tải giỏ hàng!')
        return HttpResponseRedirect(reverse('books'))


def rate_book(request, book_id):
    # Check if user is logged in
    if 'user_id' not in request.session:
        messages.warning(request, 'Vui lòng đăng nhập để đánh giá sách!')
        return HttpResponseRedirect(reverse('login'))
    
    if request.method == 'POST':
        data = {
            'book_id': book_id,
            'customer_id': request.session['user_id'],
            'rating': request.POST['rating'],
            'comment': request.POST['comment'],
        }
        try:
            r = requests.post("http://comment-rate-service:8000/reviews/", json=data)
            if r.status_code not in [200, 201]:
                print(f"Failed to post review: status {r.status_code}")
        except Exception as e:
            print(f"Error posting review: {e}")
        return HttpResponseRedirect(reverse('books'))
    return render(request, 'rate_book.html', {
        'book_id': book_id,
        'user_name': request.session.get('user_name'),
        'user_id': request.session.get('user_id')
    })