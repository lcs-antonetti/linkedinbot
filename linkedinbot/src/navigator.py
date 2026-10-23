import os
from dotenv import load_dotenv
from playwright.sync_api import expect

load_dotenv()

def doorkicker(page):
    user = os.getenv("LINKEDIN_EMAIL")
    password = os.getenv("LINKEDIN_PASSWORD")
    page.goto("https://www.linkedin.com/login/")
    campo_user=page.get_by_role("textbox", name="E-mail ou telefone")
    campo_user.fill(user)
    expect(campo_user).to_have_value(user)
    campo_password=page.get_by_role("textbox", name="Senha")
    campo_password.fill(password)
    expect(campo_password).to_have_value(password)
    page.get_by_role("button",name="Entrar",exact=True).click()

def jobfinder(page):
    campo_pesquisa=page.get_by_test_id("typehead_input")
    campo_pesquisa.fill("sjkdnajksbdkasndjkansjdnaksndajs")