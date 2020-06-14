    
def output(text)
    code = text
    print('code', code)
    ans = []
    try:
        val = exec(code)
    except:
        ans = ["THERE HAS BEEN AN ERROR PROCESSING YOUR CODE"

    print('ans', '\n'.join(ans))
    return '\n'.join(ans)