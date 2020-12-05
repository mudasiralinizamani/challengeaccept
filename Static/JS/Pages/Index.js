const tl = gsap.timeline({ defaults: { ease: "power1.out" } });

tl.to(".text", { y: "0%", duration: 1, stagger: 0.25 });
tl.to(".slider", { y: "-100%", duration: 1.5, delay: 0.5 });
tl.to(".intro", { y: "-100%", duration: 1 }, "-=1");
tl.fromTo("nav", { opacity: 0 }, { opacity: 1, duration: 1 });
tl.fromTo(".big-text", { opacity: 0 }, { opacity: 1, duration: 1 }, "-=1");


$(document).ready(function() {
    $('#title-2').animate({
        opacity: 1,
    }, 1100, function() {
        $('#title-1-heading-1').animate({
            left: 0
        }, 1000, function() {
            $('#title-1-heading-2').animate({
                bottom: 0
            }, 1000)
        })
    })
    // const intro = document.getElementById('welcome-screen')
    // intro.classList.add('is-hidden')
})

