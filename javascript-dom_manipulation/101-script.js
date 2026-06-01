document.addEventListener('DOMContentLoaded', function () {
  const btnTranslate = document.getElementById('btn_translate');
  const languageSelect = document.getElementById('language_code');
  const helloDiv = document.getElementById('hello');

  btnTranslate.addEventListener('click', function () {
    const langCode = languageSelect.value;

    if (langCode) {
      fetch('https://hellosalut.stefanbohacek.com/?lang=' + langCode)
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          helloDiv.innerHTML = data.hello;
        });
    }
  });
});
