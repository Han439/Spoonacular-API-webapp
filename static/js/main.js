
// hamburger menu
bars = document.querySelector('.bars');
closing = document.querySelector('.close');

nav = document.querySelector('.nav-bar')


bars.addEventListener('click', function(e) {
bars.classList.remove('show');
closing.classList.add('show');
nav.classList.add('transform');
nav.style.display = 'flex';
})

closing.addEventListener('click', function(e) {
closing.classList.remove('show');
bars.classList.add('show');
nav.classList.remove('transform');
nav.style.display = 'none';
})