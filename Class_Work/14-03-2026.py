'''
14-03-2026

1. Priority wise: ID, Name, CSS Selectors, XPath
2. XPath: X stands for XML Path (extendable markup language)
    -> We can traverse backward or forward
    -> Locate elements based on any element (text as well as attribute) (in partial link text or link text only anchor tag elements were located)
    -> It is used for dynamic elements
    -> Two types: Absolute and Relative

    Two Ways : Absolute and Relative

    Absolute -> Starts from roots
    Relative -> Directly jumps to the element

    XPath using attribute
    XPath using text

    Syntax:  //tagname[@attribute = 'value']

    Contains attribute
    ->//tagname[contains(@attribute, 'value')]

    Contains Text
    ->//tagname[contains(text(), 'value')]
    ->//tagname[contains(., 'value')]


'''