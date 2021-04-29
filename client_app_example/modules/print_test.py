from templates.print import Print

def test_print_pre():
    data = 2
    result = Print.pre(data)
    assert result == "<pre>2</pre>"