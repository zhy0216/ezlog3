
Zepto(function($){
    console.log("ready!");

    $("#tweet-textarea").on("keydown", function(e){
        if(e.ctrlKey && e.which === 13){
            var $textarea = $("#tweet-textarea");
            var content = $textarea.val()
            if(content !== ""){
                $.post("/api/tweet/",{
                    "content": content
                }, function(data){
                    console.log(data)
                    if(data.rcode === 200){
                        $textarea.val("");
                        $("#tweet-container").prepend(data.tweet)
                    }
                })
            }
        }
    })


    /* ---- particles.js config ---- */

    particlesJS("particles-js", {
      "particles": {
        "number": {
          "value": 75,
          "density": {
            "enable": true,
            "value_area": 800
          }
        },
        "color": {
          "value": "#b2b2b2"
        },
        "shape": {
          "type": "circle",
          "stroke": {
            "width": 0,
            "color": "#000000"
          },
          "polygon": {
            "nb_sides": 6
          },
          "image": {
            "src": "img/github.svg",
            "width": 400,
            "height": 400
          }
        },
        "opacity": {
          "value": 0.5,
          "random": true,
          "anim": {
            "enable": true,
            "speed": 1,
            "opacity_min": 0.1,
            "sync": false
          }
        },
        "size": {
          "value": 3,
          "random": true,
          "anim": {
            "enable": true,
            "speed": 40,
            "size_min": 0.1,
            "sync": false
          }
        },
        "line_linked": {
          "enable": true,
          "distance": 150,
          "color": "#7f7f7f",
          "opacity": 0.5,
          "width": 1
        },
        "move": {
          "enable": true,
          "speed": 2,
          "direction": "none",
          "random": true,
          "straight": false,
          "out_mode": "out",
          "bounce": false,
          "attract": {
            "enable": true,
            "rotateX": 600,
            "rotateY": 1200
          }
        }
      },
      "interactivity": {
        "detect_on": "canvas",
        "events": {
          "onhover": {
            "enable": true,
            "mode": "grab"
          },
          "onclick": {
            "enable": true,
            "mode": "push"
          },
          "resize": true
        },
        "modes": {
          "grab": {
            "distance": 140,
            "line_linked": {
              "opacity": 1
            }
          },
          "bubble": {
            "distance": 400,
            "size": 40,
            "duration": 2,
            "opacity": 8,
            "speed": 3
          },
          "repulse": {
            "distance": 200,
            "duration": 0.4
          },
          "push": {
            "particles_nb": 4
          },
          "remove": {
            "particles_nb": 2
          }
        }
      },
      "retina_detect": true
    });


})


