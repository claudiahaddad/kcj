/*function onYouTubeIframeAPIReady(){

 var tag = document.createElement('script');
 tag.src = "//www.youtube.com/player_api";
 var firstScriptTag = document.getElementsByTagName('script')[0];
 firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

  var train = document.getElementById("train");

  var icon = document.createElement("img");
  icon.setAttribute("id","youtube-icon");
  icon.style.cssText = "cursor:pointer;cursor:hand";
  train.appendChild(icon);

  var div = document.createElement("div");
  console.log(14+234)
  div.setAttribute("id","youtube-player");
  train.appendChild(div);

  var toggleButton = function (play) {
    var img = play ? "train.jpg" : "pause.png";
    icon.setAttribute("src","pictures/" + img);
  }



    if ( player.getPlayerState() === YT.PlayerState.PLAYING
          || player.getPlayerState() === YT.PlayerState.BUFFERING ) {
        player.pauseVideo();
      } else {
        player.playVideo();

      }
    };


 var player;
 function onYouTubeIframeAPIReady(){
   player = new YT.Player('player', {
      height: "200",
      width: "200",
      videoId: "SW1k7DObaX4",
      events: {
        "onReady": onPlayerReady,
        "onStateChange" : onPlayerStateChange
      }
    });
  }



          player.setPlaybackQuality("small");
          toggleButton(player.getPlayerState() !== YT.PlayerState.CUED);
        },
        "onStateChange": function(e) {
          if (e.date === YT.PlayerState.ENDED) {
            toggleButton(false);
          }
        }
      }
    });
    function onPlayerReady(event) {
    $("#train").click(function(){
      player.playVideo();
    });
 }
*/




$(document).ready(function() {
var train_pause = false;
}


function toggleVideo(train_pause) {
    var iframe = document.getElementById("train_vid").contentWindow;
    func = train_pause ? 'pauseVideo' : "playVideo";
    iframe.postMessage('{"event":"command","func":"' + func + '","args":""}', '*');
  }

  $('#train').click(function(){
    toggleVideo(train_pause);
    if ($(train_pause = false))
      $(train_pause = true);
    else
      $(train_pause = true);

  });


});
