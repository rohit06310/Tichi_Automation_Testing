from playwright.sync_api import Page, expect
from urllib.parse import quote
import time

#---LandingPage--

class TestLandingPage:

    BASE_URL = "https://tichi-app-webapp-stage.web.app/"

    def test_page_title(self, page: Page):                  #---1
        page.goto(self.BASE_URL)
        expect(page).to_have_title("Tichi")

    def test_logo_is_visible(self, page: Page):             #---2
        page.goto(self.BASE_URL)
        expect(page.get_by_role("img", name="Logo")).to_be_visible()

    def test_signin_button_visible(self, page: Page):       #---3
        page.goto(self.BASE_URL)
        expect(page.get_by_role("button", name="Sign In")).to_be_visible() 

    def test_signin_navigation(self, page: Page):           #---4
        page.goto(self.BASE_URL)
        page.get_by_role("button", name="Sign In").click()
        expect(page).to_have_url("https://tichi-app-webapp-stage.web.app/login")

    def test_hero_heading(self, page: Page):                #---5
        page.goto(self.BASE_URL)
        expect(page.get_by_role("heading",name="Opportunities Everywhere – Find, Post & Earn!")).to_be_visible()

    def test_key_features_section(self, page: Page):        #---6
        page.goto(self.BASE_URL)
        expect(page.get_by_role("heading",name="Key Features")).to_be_visible()

    def test_how_it_works_section(self, page: Page):        #---7
        page.goto(self.BASE_URL)
        page.get_by_text("HOW IT WORKS").scroll_into_view_if_needed()
        expect(page.get_by_text("HOW IT WORKS")).to_be_visible()

    def test_explore_opportunities(self, page: Page):       #---8
        page.goto(self.BASE_URL)
        page.get_by_text("Explore Opportunities").scroll_into_view_if_needed()
        expect(page.get_by_text("Explore Opportunities")).to_be_visible()

    def test_subscription_section(self, page: Page):        #---9
        page.goto(self.BASE_URL)
        page.get_by_text("Plans & Subscriptions").scroll_into_view_if_needed()
        expect(page.get_by_text("Plans & Subscriptions")).to_be_visible()

    def test_faq_section(self, page: Page):                 #---10
        page.goto(self.BASE_URL)
        page.get_by_text("Frequently Asked Questions").scroll_into_view_if_needed()
        expect(page.get_by_text("Frequently Asked Questions")).to_be_visible()

    def test_ready_to_get_started_section(self, page: Page):  #---11
        page.goto(self.BASE_URL)
        page.get_by_text("Ready to Get Started?").scroll_into_view_if_needed()
        expect(page.get_by_text("Ready to Get Started?")).to_be_visible()

    def test_signup_now_navigation(self, page: Page):           #---12
        page.goto(self.BASE_URL)
        page.get_by_role("button",name="Sign Up Now").scroll_into_view_if_needed()
        page.get_by_role("button",name="Sign Up Now").click()
        expect(page).to_have_url("https://tichi-app-webapp-stage.web.app/login")

    def test_terms_and_conditions(self, page: Page):            #---13
        page.goto(self.BASE_URL)
        page.get_by_role("link",name="Terms and Conditions").scroll_into_view_if_needed()
        page.get_by_role("link",name="Terms and Conditions").click()
        expect(page).to_have_url("https://tichi-app-webapp-stage.web.app/termsAndConditions")

    def test_privacy_policy(self, page: Page):                  #---14
        page.goto(self.BASE_URL)
        page.get_by_role("link",name="Privacy Policy").scroll_into_view_if_needed()
        page.get_by_role("link",name="Privacy Policy").click()
        expect(page).to_have_url("https://tichi-app-webapp-stage.web.app/privacyPolicy")

    def test_page_scroll(self, page: Page):                     #---15
        page.goto(self.BASE_URL)
        page.mouse.wheel(0, 6000)
        expect(page.get_by_text("© 2025 Tichi. All rights reserved.")).to_be_visible()

#---LoginPage---

class TestLoginPage:

    email = "rohitk06102005@gmail.com"
    encoded_email = quote(email)

    BASE_URL = "https://tichi-app-webapp-stage.web.app/"

    def test_login_page_loads(self, page: Page):                #---1
        page.goto(f"{self.BASE_URL}/login")
        expect(page).to_have_title("Tichi")

    def test_email_field_is_visible(self, page: Page):          #---2
        page.goto(f"{self.BASE_URL}/login")
        expect(page.get_by_placeholder("Email Address")).to_be_visible()

    def test_continue_button_is_visible(self, page: Page):      #---3
        page.goto(f"{self.BASE_URL}/login")
        expect(page.get_by_role("button", name="Continue",exact=True)).to_be_visible()

    def test_empty_email_validation(self, page: Page):          #---4
        page.goto(f"{self.BASE_URL}/login")
        page.get_by_role("button", name="Continue",exact=True).click()
        expect(page.get_by_text("Email is required")).to_be_visible()

    def test_invalid_email_validation(self, page: Page):        #---5
        page.goto(f"{self.BASE_URL}/login")
        page.get_by_placeholder("Email Address").fill("abc@gmail.com")
        page.get_by_role("button", name="Continue",exact=True).click()
        expect(page.get_by_text("Invalid email")).to_be_visible()

    def test_registered_email_moves_to_password_page(self, page: Page): #---6
        page.goto(f"{self.BASE_URL}/login")
        page.get_by_placeholder("Email Address").fill("rohitk06102005@gmail.com")
        page.get_by_role("button", name="Continue",exact=True).click()
        expect(page.get_by_placeholder("Password")).to_be_visible()

    def test_password_field_visible(self, page: Page):          #---7
        page.goto(f"{self.BASE_URL}/login")
        page.get_by_placeholder("Email Address").fill("rohitk06102005@gmail.com")
        page.get_by_role("button", name="Continue",exact=True).click()
        expect(page.get_by_placeholder("Password")).to_be_visible()

    def test_password_visibility_toggle(self, page: Page):      #---8
        page.goto(f"{self.BASE_URL}/login")
        page.get_by_placeholder("Email Address").fill("rohitk06102005@gmail.com")
        page.get_by_role("button", name="Continue",exact=True).click()
        page.locator("button").filter(has=page.locator("svg")).click()

    def test_empty_password_validation(self, page: Page):       #---9
        page.goto(f"{self.BASE_URL}/login")
        page.get_by_placeholder("Email Address").fill("rohitk06102005@gmail.com")
        page.get_by_role("button", name="Continue",exact=True).click()
        page.get_by_role("button", name="Login").click()
        expect(page.get_by_text("Password is required")).to_be_visible()

    def test_invalid_password(self, page: Page):                #---10
        page.goto(f"{self.BASE_URL}/login")
        page.get_by_placeholder("Email Address").fill("rohitk06102005@gmail.com")
        page.get_by_role("button", name="Continue",exact=True).click()
        page.get_by_placeholder("Password").fill("WrongPassword123")
        page.get_by_role("button", name="Login").click()
        expect(page.get_by_text("Invalid password")).to_be_visible()

    def test_successful_login(self, page: Page):                #---11
        page.goto(f"{self.BASE_URL}/login")
        page.get_by_placeholder("Email Address").fill("rohitk06102005@gmail.com")
        page.get_by_role("button", name="Continue",exact=True).click()
        page.get_by_placeholder("Password").fill("RohitVishal@2005")
        page.get_by_role("button", name="Login").click()
        expect(page).not_to_have_url(f"{self.BASE_URL}/login")

    def test_forgot_password_navigation(self, page: Page):      #---12
        page.goto(f"{self.BASE_URL}/login")
        page.get_by_placeholder("Email Address").fill("rohitk06102005@gmail.com")
        expect(page.get_by_placeholder("Email Address")).to_have_value("rohitk06102005@gmail.com")
        page.get_by_role("button", name="Continue",exact=True).click()
        page.get_by_text("Forgot Password?").click()
        expect(page).to_have_url(f"{self.BASE_URL}forgot-password?email={self.encoded_email}")
        
#--SignUp Page---
class TestSignupPage:

    BASE_URL = "https://tichi-app-webapp-stage.web.app"
    def goto_signup(self, page: Page):
        page.goto(f"{self.BASE_URL}/sign-up")
    # ---------- TC_01 ----------
    def test_signup_page_load(self, page: Page):
        self.goto_signup(page)
        expect(page).to_have_url(f"{self.BASE_URL}/sign-up")
        expect(page.get_by_role("heading", name="Sign Up to Tichi")).to_be_visible()


    # ---------- TC_02 ----------
    def test_signup_ui_elements(self, page: Page):
        self.goto_signup(page)
        expect(page.get_by_placeholder("Enter your first name")).to_be_visible()
        expect(page.get_by_placeholder("Enter your last name")).to_be_visible()
        expect(page.get_by_placeholder("Enter your phone number")).to_be_visible()
        expect(page.get_by_placeholder("Enter your email address")).to_be_visible()
        expect(page.get_by_placeholder("Enter your password")).to_be_visible()
        expect(page.get_by_placeholder("Enter your confirm password")).to_be_visible()
        expect(page.locator("input[type='checkbox']")).to_be_visible()
        expect(page.get_by_role("button", name="Sign Up")).to_be_visible()


    # ---------- TC_03 ----------
    def test_empty_signup(self, page: Page):
        self.goto_signup(page)
        page.get_by_role("button", name="Sign Up").click()
        expect(page).to_have_url(f"{self.BASE_URL}/sign-up")

    # ---------- TC_04 ----------
    def test_invalid_email(self, page: Page):
        self.goto_signup(page)
        page.get_by_placeholder("Enter your first name").fill("Rohit")
        page.get_by_placeholder("Enter your last name").fill("K")
        page.get_by_placeholder("Enter your phone number").fill("6384579625")
        page.get_by_placeholder("Enter your email address").fill("abcd.com")
        page.get_by_placeholder("Enter your password").fill("Password@123")
        page.get_by_placeholder("Enter your confirm password").fill("Password@123")
        page.locator("input[type='checkbox']").check()
        page.get_by_role("button", name="Sign Up").click()
        expect(page).to_have_url(f"{self.BASE_URL}/sign-up")


    # ---------- TC_05 ----------
    def test_password_mismatch(self, page: Page):
        self.goto_signup(page)
        page.get_by_placeholder("Enter your first name").fill("Rohit")
        page.get_by_placeholder("Enter your last name").fill("K")
        page.get_by_placeholder("Enter your phone number").fill("6384579625")
        page.get_by_placeholder("Enter your email address").fill("rohit06102005@gmail.com")
        page.get_by_placeholder("Enter your password").fill("Password@123")
        page.get_by_placeholder("Enter your confirm password").fill("Password@321")
        page.locator("input[type='checkbox']").check()
        page.get_by_role("button", name="Sign Up").click()
        expect(page.get_by_text("Passwords do not match")).to_be_visible()

    # ---------- TC_06 ----------
    def test_existing_email(self, page: Page):
        self.goto_signup(page)
        page.get_by_placeholder("Enter your first name").fill("Rohit")
        page.get_by_placeholder("Enter your last name").fill("K")
        page.get_by_placeholder("Enter your phone number").fill("6384579625")
        page.get_by_placeholder("Enter your email address").fill("rohitk06102005@gmail.com")
        page.get_by_placeholder("Enter your password").fill("RohitVishal@2005")
        page.get_by_placeholder("Enter your confirm password").fill("RohitVishal@2005")
        page.locator("input[type='checkbox']").check()
        page.get_by_role("button", name="Sign Up").click()
        expect(page.get_by_text("User Already Exists")).to_be_visible()


    # ---------- TC_07 ----------
    def test_terms_and_privacy_links_visible(self, page: Page):
        self.goto_signup(page)
        expect(page.get_by_text("Terms and conditions")).to_be_visible()
        expect(page.get_by_text("Privacy Policy")).to_be_visible()


    # ---------- TC_08 ----------
    def test_successful_signup(self, page: Page):
        self.goto_signup(page)
        unique_email = f"rohit{int(time.time())}@gmail.com"
        page.get_by_placeholder("Enter your first name").fill("Rohit")
        page.get_by_placeholder("Enter your last name").fill("K")
        page.get_by_placeholder("Enter your phone number").fill("6384579625")
        page.get_by_placeholder("Enter your email address").fill(unique_email)
        page.get_by_placeholder("Enter your password").fill("RohitVishal@2005")
        page.get_by_placeholder("Enter your confirm password").fill("RohitVishal@2005")
        page.locator("input[type='checkbox']").check()
        page.get_by_role("button", name="Sign Up").click()
        expect(page).not_to_have_url(f"{self.BASE_URL}/sign-up")


#---Forgot Password Page

class TestForgotPassword:

    BASE_URL = "https://tichi-app-webapp-stage.web.app"

    email = "rohitk06102005@gmail.com"
    encoded_email = quote(email)

    def goto_forgot_password(self, page: Page):                 #---1
        page.goto(f"{self.BASE_URL}/login")
        page.get_by_placeholder("Email Address").fill("rohitk06102005@gmail.com")
        page.get_by_role("button",name="Continue",exact=True).click()
        page.get_by_text("Forgot Password?").click()

    def test_forgot_password_page_loads(self, page: Page):      #---2
        self.goto_forgot_password(page)
        expect(page).to_have_url(f"{self.BASE_URL}/forgot-password?email={self.encoded_email}")

    def test_email_field_visible(self, page: Page):             #---3
        self.goto_forgot_password(page)
        expect(page.get_by_placeholder("Email Address")).to_be_visible()

    def test_send_verification_button_visible(self, page: Page):#---4
        self.goto_forgot_password(page)
        expect(page.get_by_role("button",name="Send Verification")).to_be_visible()

    def test_empty_email_validation(self, page: Page):          #---5
        self.goto_forgot_password(page)
        page.get_by_placeholder("Email Address").clear()
        page.get_by_role("button",name="Send Verification").click()
        expect(page.get_by_text("Email is required")).to_be_visible()

    def test_invalid_email(self, page: Page):                   #---6
        self.goto_forgot_password(page)
        page.get_by_placeholder("Email Address").fill("abc.com")
        page.get_by_role("button",name="Send Verification").click()
        expect(page.get_by_text("Invalid email")).to_be_visible()

    def test_registered_email(self, page: Page):                #---7
        self.goto_forgot_password(page)
        email = page.get_by_placeholder("Enter your email address")
        expect(email).to_have_value("rohitk06102005@gmail.com")
        page.get_by_role("button",name="Send Verification").click()
        expect(page.get_by_text("Check your Email")).to_be_visible()

    def test_back_button(self, page: Page):                     #---8
        self.test_registered_email(page)
        page.get_by_role("button",name="Back").click()
        expect(page).to_have_url(f"{self.BASE_URL}/login")

#---Logout Page---



class TestLogoutPage:

    BASE_URL = "https://tichi-app-webapp-stage.web.app"
    EMAIL = "rohitk06102005@gmail.com"
    PASSWORD = "RohitVishal@2005"

    # ---------------- Login Helper ---------------- #

    def login(self, page: Page):
        page.goto(f"{self.BASE_URL}/login")
        page.get_by_placeholder("Email Address").fill(self.EMAIL)
        page.get_by_role( "button",name="Continue",exact=True).click()
        page.get_by_placeholder("Password").fill(self.PASSWORD)
        page.get_by_role("button",name="Login").click()
        expect(page).to_have_url(f"{self.BASE_URL}/home")


    # ---------------- TC_01 ---------------- #

    def test_profile_icon_visible(self, page: Page):
        self.login(page)
        expect(page.get_by_alt_text("Profile")).to_be_visible()


    # ---------------- TC_02 ---------------- #

    def test_open_profile_menu(self, page: Page):
        self.login(page)
        page.get_by_alt_text("Profile").click()
        expect(page.get_by_role("button", name="Sign Out")).to_be_visible()


    # ---------------- TC_03 ---------------- #

    def test_logout_popup(self, page: Page):
        self.login(page)
        page.get_by_alt_text("Profile").click()
        page.get_by_role("button",name="Sign Out").click()
        expect(page.get_by_text("Are you sure you want to sign out?")).to_be_visible()


    # ---------------- TC_04 ---------------- #

    def test_cancel_logout(self, page: Page):
        self.login(page)
        page.get_by_alt_text("Profile").click()
        page.get_by_role("button",name="Sign Out").click()
        page.get_by_role("button",name="Cancel").click()
        expect(page).to_have_url(f"{self.BASE_URL}/home")


    # ---------------- TC_05 ---------------- #

    def test_successful_logout(self, page: Page):
        self.login(page)
        page.get_by_alt_text("Profile").click()
        page.get_by_role("button",name="Sign Out").click()
        page.get_by_role("button",name="Sign Out",exact=True).click()
        expect(page).to_have_url(f"{self.BASE_URL}/login")
        expect(page.get_by_role("heading",name="Sign in to Tichi")).to_be_visible()

    # ---------------- TC_06 ---------------- #

    def test_back_button_after_logout(self, page: Page):
        self.login(page)
        page.get_by_alt_text("Profile").click()
        page.get_by_role( "button",name="Sign Out").click()
        page.get_by_role("button",name="Sign Out",exact=True).click()
        page.go_back()
        expect(page).to_have_url(f"{self.BASE_URL}/login")