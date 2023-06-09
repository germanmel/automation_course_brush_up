from selenium.webdriver.common.by import By

class TextBoxPageLocators:

    #fields
    FULL_NAME = (By.CSS_SELECTOR, '#userName')
    EMAIL = (By.CSS_SELECTOR, '#userEmail')
    CURRENT_ADRESS = (By.CSS_SELECTOR, '#currentAddress')
    PERMANENT_ADRESS = (By.CSS_SELECTOR, '#permanentAddress')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '#submit')

    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADRESS = (By.CSS_SELECTOR, '#output #permanentAddress')

class CheckBoxLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    ITEM_LIST = (By.CSS_SELECTOR, '.rct-title')
    CHECKED_ITEMS = (By.CSS_SELECTOR, '.rct-icon-check')
    ITEM_TITLE = (By.XPATH, ".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULTS = (By.CSS_SELECTOR, '.text-success')

class RadioButtonLocators:
    YES_RADIOBUTTON = (By.CSS_SELECTOR, '.custom-control-label[for="yesRadio"]')
    IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, '.custom-control-label[for="impressiveRadio"]')
    NO_RADIOBUTTON = (By.CSS_SELECTOR, '.custom-control-label[for="noRadio"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, '.text-success')

class WebTableLocators:
    #add person form
    ADD_BUTTON = (By.CSS_SELECTOR, '#addNewRecordButton')
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, '#firstName')
    LASTNAME_INPUT = (By.CSS_SELECTOR, '#lastName')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#userEmail')
    AGE_INPUT = (By.CSS_SELECTOR, '#age')
    SALARY_INPUT = (By.CSS_SELECTOR, '#salary')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, '#department')
    SUBMIT = (By.CSS_SELECTOR, '#submit')

    #table
    FULL_PERSONS_LIST = (By.CSS_SELECTOR, 'div[class="rt-tr-group"]')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    ROW_PARENT = (By.XPATH, './/ancestor::div[@class="rt-tr-group"]')

    #update
    UPDATE_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')
    NO_ROWS_FOUND = (By.CSS_SELECTOR, 'div[class="rt-noData"]')
    CHANGE_ROWS_DROPDOWN = (By.TAG_NAME, 'select')

class ButtonsPageLocators:
    #buttons
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, 'button[id="doubleClickBtn"]')
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, 'button[id="rightClickBtn"]')
    CLICK_ME_BUTTON = (By.XPATH, '//div[3]/button')

    #success messages
    SUCCESS_DOUBLE = (By.CSS_SELECTOR, 'p[id="doubleClickMessage"]')
    SUCCESS_RIGHT = (By.CSS_SELECTOR, 'p[id="rightClickMessage"]')
    SUCCESS_CLICK_ME = (By.CSS_SELECTOR, 'p[id="dynamicClickMessage"]')

class LinkPageLocators:
    SIMPLE_HOME_LINK = (By.CSS_SELECTOR, 'a[id="simpleLink"]')
    DYNAMIC_HOME_LINK = (By.CSS_SELECTOR, 'a[id="dynamicLink"]')
    CREATED = (By.CSS_SELECTOR, 'a[id="created"]')
    NO_CONTENT = (By.CSS_SELECTOR, 'a[id="no-content"]')
    MOVED = (By.CSS_SELECTOR, 'a[id="moved"]')
    BAD_REQUEST =  (By.CSS_SELECTOR, 'a[id="bad-request"]')
    UNAUTHORIZED = (By.CSS_SELECTOR, 'a[id="unauthorized"]')
    FORBIDDEN = (By.CSS_SELECTOR, 'a[id="forbidden"]')
    NOT_FOUND = (By.CSS_SELECTOR, 'a[id="invalid-url"]')

class FilePageLocators:
    UPLOAD_FILE = (By.CSS_SELECTOR, 'input[id="uploadFile"]')
    UPLOADED_RESULT = (By.CSS_SELECTOR, 'p[id="uploadedFilePath"]')
    DOWNLOAD_BUTTON = (By.CSS_SELECTOR, 'a[id="downloadButton"]')

class DynamicPropertiesPageLocators:
    DISABLED_BUTTON = (By.CSS_SELECTOR, 'button[id="enableAfter"]')
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, 'button[id="colorChange"]')
    VISIBLE_AFTER_5SEC_BUTTON = (By.CSS_SELECTOR, 'button[id="visibleAfter"]')


