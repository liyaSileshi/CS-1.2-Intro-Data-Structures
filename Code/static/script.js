$(document).ready(function(){
    $('.update').on('click', function(){
      req = $.ajax({
            url: '/',
            type: 'GET'
      });
    });
  });