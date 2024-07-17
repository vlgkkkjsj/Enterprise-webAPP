document.addEventListener('DOMContentLoaded', function() {
    const paginationLinks = document.querySelectorAll('.pagination a');
    const searchInput = document.querySelector('input[name="q"]');

    paginationLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const url = new URL(this.href);
            const params = new URLSearchParams(url.search);
            params.set('q', searchInput.value);
            window.location.href = `${url.pathname}?${params.toString()}`;
        });
    });
    
    const searchButton = document.querySelector('button[type="submit"]');
    searchButton.addEventListener('click', function() {
        searchButton.classList.add('button-click-animation');
        setTimeout(() => {
            searchButton.classList.remove('button-click-animation');
        }, 200);
    });

    $('#deleteModal').on('show.bs.modal', function(event) {
        const button = $(event.relatedTarget);
        const url = button.data('url');
        const modal = $(this);
        modal.find('form').attr('action', url);
    });
});

