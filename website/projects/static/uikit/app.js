// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  hljs.highlightAll();
});

let alertWraper = document.querySelector('.alert')
let alertClose = document.querySelector('.alert__close')

if (alertWraper) {
  alertClose.addEventListener('click', () =>
    alertWraper.style.display = 'none'
  )
}
