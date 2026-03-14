'''
13-03-2026 (Friday)

1. Anchor tag in html <a href="http..."></a>
2. find_element(locator_name, locator_value)
    -> single elements,
    -> returns 1 single web element
    -> NoSuchElement Exception
3. find_elements(locator_name, locator_value)
    -> multiple elements
    -> returns list of web elements
    -> [] empty list for no element

4. Locator - address of an element
    Locator are of 8 types:
    -> ID
    -> Name
    -> CLASS NAME
    -> TAG NAME
    -> LINK TEXT
    -> PARTIAL LINK TEXT
    -> CSS SELECTORS
    -> XPATH

    Two actions we'll perfom now
    -> click()
    -> send_keys('keys')

    If we use TAG_NAME
    then it will assign the first Tag name of that page
    Similar for the class name (replace " " with dot)

    Link Tag: Only work on anchor tag
    Partial Link Tag: Any Partial Name from the screen

    CSS SELECTORS:
    <input id='link', type ='text'>

    "tagName[attribute= 'value']"

'''