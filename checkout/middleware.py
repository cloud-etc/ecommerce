from .models import CartItem


def cart_item_middleware(get_response):

    def middleware(request):

        session_key = request.session.session_key
        print("antes")
        response = get_response(request)
        print("depois")
        if session_key != request.session.session_key:
            CartItem.objects.filter(cart_key=session_key).update(
                cart_key=request.session.session_key
            )

        return response

    return middleware