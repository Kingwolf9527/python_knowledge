#coding=utf-8


Feature: Register User

    Scenario: open register website

        When I open the register website
        Then I expect that the title is "注册"


    Scenario: input userinfo

        When I set with useremail "test5475@163.com"
        And I set with userename "tes75475"
        And I set with password "tes545475"
        And I set with captcha_code "dehj5"
        And I click with register_button
        Then I expect that text is "验证码错误"

