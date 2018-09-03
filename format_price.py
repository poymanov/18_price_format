def format_price(price):
    try:
        return '{:_.0f}'.format(float(price)).replace('_', ' ')
    except ValueError:
        return None


if __name__ == '__main__':
    price = input('Enter the price to format: ')
    formatted_price = format_price(price)

    if not formatted_price:
        print('Failed to format price string')
    else:
        print('Formatted price: {}'.format(formatted_price))
