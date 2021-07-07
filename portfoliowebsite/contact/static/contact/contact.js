function alertMessage(text) {
    alert(text);
};

function recaptchatoken(recaptcha_site_key){
    grecaptcha.ready(function() {
        grecaptcha.execute(recaptcha_site_key, {action: "/contact/"}).then(function(token) {
            document.getElementById('g-recaptcha-response').value = token;
        });
    });
};