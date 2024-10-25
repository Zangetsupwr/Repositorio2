const handleAlert = () => {
    alert("Busca a tus amigos y reparte a través de nuesta página abrazos a todos");
}
const handleAcceptCookies = () => {
    const cookies = document.querySelector('.cookies');
    cookies.style.display = 'none'; // Ocultar el elemento
}
const handleLike = (element) => {
    const parent = element.parentElement;
    const abrazos = parent.querySelector("p");
    let num = parseInt(abrazos.dataset.hugs);
    num++;
    abrazos.dataset.hugs = num;
    abrazos.innerHTML = `${num} abrazo(s)`;
}