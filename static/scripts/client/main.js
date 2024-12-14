(function () {

    new HSShowAnimation('.js-animation-link');
    new HSMegaMenu('.js-mega-menu', {
        desktop: {
            position: 'left'
        }
    });
    HSBsDropdown.init();

    HSBsValidation.init('.js-validate-login', {
        onSubmit: data => {
            data.event.preventDefault();
            data.event.stopPropagation();

            const formData = new FormData(data.form);
            const action = data.form.getAttribute('action');
            const method = data.form.getAttribute('method');

            fetch(action, {
                method: method,
                body: formData
            })
                .then(response => response.json())
                .then(data1 => {
                    if (data1.success) {
                        showAlert(data1.message, 'success')
                    } else {
                        showAlert(data1.message, 'error')
                    }
                    if (data1.success) {
                        // set user_id to cookie
                        document.cookie = `user_id=${data1.data.user_id}; path=/`;

                        if (data1?.data?.role === 'ADMIN') {
                            window.location.href = '/admin';
                        } else {
                            window.location.href = '/';
                        }
                    }
                })
                .catch(error => {
                    showAlert(error, 'error');
                });
        }
    });

    HSBsValidation.init('.js-validate-register', {
        onSubmit: data => {
            data.event.preventDefault();
            data.event.stopPropagation();

            const formData = new FormData(data.form);
            const action = data.form.getAttribute('action');
            const method = data.form.getAttribute('method');

            fetch(action, {
                method: method,
                body: formData
            })
                .then(response => response.json())
                .then(data1 => {
                    if (data1.success) {
                        showAlert(data1.message, 'success');
                    } else {
                        showAlert(data1.message, 'error');
                    }
                })
                .catch(error => {
                    showAlert(error, 'error');
                });
        }
    });

    HSBsValidation.init('.js-validate-checkout', {
        onSubmit: data => {
            data.event.preventDefault();
            data.event.stopPropagation();

            const formData = new FormData(data.form);
            const action = data.form.getAttribute('action');
            const method = data.form.getAttribute('method');

            fetch(action, {
                method: method,
                body: formData
            })
                .then(response => response.json())
                .then(data1 => {
                    window.location.href = data1.link;
                })
                .catch(error => {
                    showAlert(error, 'error');
                });
        }
    });

    HSBsValidation.init('.js-validate-forget', {
        onSubmit: data => {
            data.event.preventDefault();
            data.event.stopPropagation();

            toast.classList.remove('bg-danger');
            toast.classList.remove('bg-success');
            toast.classList.add('bg-warning');
            message.textContent = 'Vui lòng liên hệ với quản trị viên để lấy lại mật khẩu';
            liveToast.show();
        }
    });
    // INITIALIZATION OF GO TO
    // =======================================================
    new HSGoTo('.js-go-to');


    // INITIALIZATION OF SWIPER
    // =======================================================
    var sliderThumbs = new Swiper('.js-swiper-shop-hero-thumbs', {
        watchSlidesVisibility: true,
        watchSlidesProgress: true,
        history: false,
        slidesPerView: 3,
        spaceBetween: 15,
        on: {
            beforeInit: (swiper) => {
                const css = `.swiper-slide-thumb-active .swiper-thumb-progress .swiper-thumb-progress-path {
                                                          opacity: 1;
                                                          -webkit-animation: ${swiper.originalParams.autoplay.delay}ms linear 0ms forwards swiperThumbProgressDash;
                                                          animation: ${swiper.originalParams.autoplay.delay}ms linear 0ms forwards swiperThumbProgressDash;
                                                      }`
                style = document.createElement('style')
                document.head.appendChild(style)
                style.type = 'text/css'
                style.appendChild(document.createTextNode(css));

                swiper.el.querySelectorAll('.js-swiper-thumb-progress')
                    .forEach(slide => {
                        slide.insertAdjacentHTML('beforeend', '<span class="swiper-thumb-progress"><svg version="1.1" viewBox="0 0 160 160"><path class="swiper-thumb-progress-path" d="M 79.98452083651917 4.000001576345426 A 76 76 0 1 1 79.89443752470656 4.0000733121155605 Z"></path></svg></span>')
                    })
            },
        },
    });

    var swiper = new Swiper('.js-swiper-shop-classic-hero', {
        autoplay: true,
        loop: true,
        navigation: {
            nextEl: '.js-swiper-shop-classic-hero-button-next',
            prevEl: '.js-swiper-shop-classic-hero-button-prev',
        },
        thumbs: {
            swiper: sliderThumbs
        }
    });

    HSCore.components.HSMask.init('.js-input-mask')

    // INITIALIZATION OF COUNTDOWN
    // =======================================================
    const oneYearFromNow = new Date()

    document.querySelectorAll('.js-countdown').forEach(item => {
        const days = item.querySelector('.js-cd-days'),
            hours = item.querySelector('.js-cd-hours'),
            minutes = item.querySelector('.js-cd-minutes'),
            seconds = item.querySelector('.js-cd-seconds')

        countdown(oneYearFromNow.setFullYear(
                oneYearFromNow.getFullYear() + 1),
            ts => {
                days.innerHTML = ts.days
                hours.innerHTML = ts.hours
                minutes.innerHTML = ts.minutes
                seconds.innerHTML = ts.seconds
            },
            countdown.DAYS | countdown.HOURS | countdown.MINUTES | countdown.SECONDS
        )
    })
})();

document.addEventListener('DOMContentLoaded', function () {
    const currentPath = window.location.pathname;
    const menuItems = document.querySelectorAll('.nav-item a.nav-link');

    menuItems.forEach(function (menuItem) {
        if (menuItem.getAttribute('href') === currentPath) {
            menuItem.classList.add('active');
        }
    });
});