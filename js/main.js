$(window).on('load', function () {
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const smallScreen = window.matchMedia('(max-width: 767px)').matches;

    if (!reduceMotion && !smallScreen && $.fn.vide) {
        $('#header').vide('./video/cover', {
            bgColor: '#111111',
            position: '50% 50%'
        });
    }
});
