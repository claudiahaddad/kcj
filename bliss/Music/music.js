$(document).ready(function() {
var train_pause = true;

function toggleVideo(train_ispaused, video_name) {
    var iframe = document.getElementById(video_name).contentWindow;
    func = train_ispaused ?  "playVideo" : 'pauseVideo';
    iframe.postMessage('{"event":"command","func":"' + func + '","args":""}', '*');
  }

  $('#train').click(function(){
    toggleVideo(train_pause, "train_vid");
    if (train_pause == true) {
      $(train_pause = false); }
    else {
      $(train_pause = true);
    }
  });
});


$(document).ready(function() {
var vid_vid = true;

function toggleVideo(vid_ispaused, video_name) {
    var iframe = document.getElementById(video_name).contentWindow;
    func = vid_ispaused ?  "playVideo" : 'pauseVideo';
    iframe.postMessage('{"event":"command","func":"' + func + '","args":""}', '*');
  }

  $('#coffee').click(function(){
    toggleVideo(vid_vid, "coffee_vid");
    if (vid_vid == true) {
      $(vid_vid = false); }
    else {
      $(vid_vid = true);
    }
  });
});


$(document).ready(function() {
var vid_vid = true;

function toggleVideo(vid_ispaused, video_name) {
    var iframe = document.getElementById(video_name).contentWindow;
    func = vid_ispaused ?  "playVideo" : 'pauseVideo';
    iframe.postMessage('{"event":"command","func":"' + func + '","args":""}', '*');
  }

  $('#ocean').click(function(){
    toggleVideo(vid_vid, "ocean_vid");
    if (vid_vid == true) {
      $(vid_vid = false); }
    else {
      $(vid_vid = true);
    }
  });
});


$(document).ready(function() {
var vid_vid = true;

function toggleVideo(vid_ispaused, video_name) {
    var iframe = document.getElementById(video_name).contentWindow;
    func = vid_ispaused ?  "playVideo" : 'pauseVideo';
    iframe.postMessage('{"event":"command","func":"' + func + '","args":""}', '*');
  }

  $('#birds').click(function(){
    toggleVideo(vid_vid, "birds_vid");
    if (vid_vid == true) {
      $(vid_vid = false); }
    else {
      $(vid_vid = true);
    }
  });
});


$(document).ready(function() {
var vid_vid = true;

function toggleVideo(vid_ispaused, video_name) {
    var iframe = document.getElementById(video_name).contentWindow;
    func = vid_ispaused ?  "playVideo" : 'pauseVideo';
    iframe.postMessage('{"event":"command","func":"' + func + '","args":""}', '*');
  }

  $('#volcano').click(function(){
    toggleVideo(vid_vid, "volcano_vid");
    if (vid_vid == true) {
      $(vid_vid = false); }
    else {
      $(vid_vid = true);
    }
  });
});




$(document).ready(function() {
var vid_vid = true;

function toggleVideo(vid_ispaused, video_name) {
    var iframe = document.getElementById(video_name).contentWindow;
    func = vid_ispaused ?  "playVideo" : 'pauseVideo';
    iframe.postMessage('{"event":"command","func":"' + func + '","args":""}', '*');
  }

  $('#beach').click(function(){
    toggleVideo(vid_vid, "beach_vid");
    if (vid_vid == true) {
      $(vid_vid = false); }
    else {
      $(vid_vid = true);
    }
  });
});


$(document).ready(function() {
var vid_vid = true;

function toggleVideo(vid_ispaused, video_name) {
    var iframe = document.getElementById(video_name).contentWindow;
    func = vid_ispaused ?  "playVideo" : 'pauseVideo';
    iframe.postMessage('{"event":"command","func":"' + func + '","args":""}', '*');
  }

  $('#wind').click(function(){
    toggleVideo(vid_vid, "wind_vid");
    if (vid_vid == true) {
      $(vid_vid = false); }
    else {
      $(vid_vid = true);
    }
  });
});


$(document).ready(function() {
var vid_vid = true;

function toggleVideo(vid_ispaused, video_name) {
    var iframe = document.getElementById(video_name).contentWindow;
    func = vid_ispaused ?  "playVideo" : 'pauseVideo';
    iframe.postMessage('{"event":"command","func":"' + func + '","args":""}', '*');
  }

  $('#thunder').click(function(){
    toggleVideo(vid_vid, "thunder_vid");
    if (vid_vid == true) {
      $(vid_vid = false); }
    else {
      $(vid_vid = true);
    }
  });
});


$(document).ready(function() {
var vid_vid = true;

function toggleVideo(vid_ispaused, video_name) {
    var iframe = document.getElementById(video_name).contentWindow;
    func = vid_ispaused ?  "playVideo" : 'pauseVideo';
    iframe.postMessage('{"event":"command","func":"' + func + '","args":""}', '*');
  }

  $('#happy').click(function(){
    toggleVideo(vid_vid, "happy_vid");
    if (vid_vid == true) {
      $(vid_vid = false); }
    else {
      $(vid_vid = true);
    }
  });
});


$(document).ready(function() {
var vid_vid = true;

function toggleVideo(vid_ispaused, video_name) {
    var iframe = document.getElementById(video_name).contentWindow;
    func = vid_ispaused ?  "playVideo" : 'pauseVideo';
    iframe.postMessage('{"event":"command","func":"' + func + '","args":""}', '*');
  }

  $('#reflective').click(function(){
    toggleVideo(vid_vid, "reflective_vid");
    if (vid_vid == true) {
      $(vid_vid = false); }
    else {
      $(vid_vid = true);
    }
  });
});
