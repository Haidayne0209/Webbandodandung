function goToPage(categoryId) {
    window.location.href = `/products?cate=${categoryId}`;
}

function filter() {
    const textSearch = document.getElementById('text-search').value;
    const urlParams = new URLSearchParams(window.location.search);
    const categoryId = urlParams.get('cate') || '-1';

    window.location.href = `/products?cate=${categoryId}&key=${textSearch}`;
}

function sort(element) {
    console.log(element.value);
    const urlParams = new URLSearchParams(window.location.search);
    window.location.href = `/products`;
}

new HSQuantityCounter('.js-quantity-counter');