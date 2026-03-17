    # Ctrl + F to open search bar in the Inspect section of a website

'''
Traversing Using XPath
    ->Forward
    //div/input

    ->Backward
    //input/..

    To locate Dynamic Element using a static element

    1. Identify State
    2. Move to common Parent
    3. Fetch dynamic element

    e.g -> //td[text()='Cantrell']/..//td[6]

    ~ Third Action to perform on find_element function
    salary = driver.find_element(By.XPATH, "//td[text()='Cantrell']/../td[6]")
    print(salary.text)
    -> " .text "

    ~ It will keep the browser close and perform the action that are mention in script
    o.add_argument("headless")

    
    Sibling Traversing
     -> Following Sibling
     -> Preceding Sibling
    
    <tr>
    <td> U/A </td>
    <td>Dhurandar 2</td>
    <td>***</td>
    <td>10Cr</td>
    </tr>
    
    td[text()='Dhurandar 2'//following-siblings::td[2]

    td[text()='Dhurandar 2'//preceding-siblings::td[2=1]

'''