/**
 * [slider description]
 * @param  {[type]} el      [description]
 * @param  {[type]} options [description]
 * @return {[type]}         [description]
 */
$.om = $.om || {};
$.om.slider = function(el, options) {

  'use strict';

  var base = this;
  base.init = function() {
    options = $.extend({
      slider: null,
      dots: null,
      next: null,
      pre: null,
      index: 0,
      timer: 5000,
      showtime: 800
    }, options || {});
    var s,
      inbox = options.slider.find('ul>li'),
      size = inbox.size(),
      b = options.index,
      play = 1,
      movelist = options.dots;

    function move() {
      b++;
      if (b > size - 1) {
        b = 0;
      }
      inbox.each(function(e) {
        inbox.eq(e).hide(0);
        movelist.find("a").eq(e).removeClass("cur");
        if (e == b) {
          inbox.eq(b).fadeIn(options.showtime);
          movelist.find("a").eq(b).addClass("cur");
        }
      });
    }
    s = setInterval(move, options.timer);

    function stopp(obj) {
      $(obj).hover(function() {
        if (play) {
          clearInterval(s);
          play = 0;
        }
      }, function() {
        if (!play) {
          s = setInterval(move, options.timer);
          play = 1;
        }
      });
    }

    if (options.next === null || options.pre === null) {
      options.slider.find('.arrow').hide()
    } else {
      options.next.click(function() {
        move();
      });

      options.pre.click(function() {
        b--;
        if (b < 0) {
          b = size - 1
        }
        inbox.each(function(e) {
          inbox.eq(e).hide(0);
          movelist.find("a").eq(e).removeClass("cur");
          if (e == b) {
            inbox.eq(b).fadeIn(options.showtime);
            movelist.find("a").eq(b).addClass("cur");
          }
        });
      });

      options.slider.hover(function() {
        options.next.fadeIn();
        options.pre.fadeIn();
      }, function() {
        options.next.fadeOut();
        options.pre.fadeOut();
      });

    }

    movelist.find("a").click(function() {
      var rel = $(this).attr("rel");
      inbox.each(function(e) {
        inbox.eq(e).hide(0);
        movelist.find("a").eq(e).removeClass("cur");
        if (e == rel) {
          inbox.eq(rel).fadeIn(options.showtime);
          movelist.find("a").eq(rel).addClass("cur");
        }
      });
    });

    inbox.each(function(e) {
      var inboxsize = inbox.size();
      var inboxwimg = $(this).find('img').width();
      inbox.eq(e).css({
        "margin-left": (-1) * inboxwimg / 2 + "px",
        "z-index": inboxsize - e
      });
    });

  }
}

$.fn.omSlider = function(options) {
  return this.each(function() {
    new $.om.slider(this, options).init();
  });
};
