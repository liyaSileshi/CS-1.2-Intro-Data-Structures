$(document).ready(function(){
    $('#form').on('submit', function(e){
      // req = $.ajax({
      //       url: '/',
      //       type: 'GET',
      //       success: res => {
      //         alert(res)
      //       }
      // });
      $.get("/",(data,status) => {
        alert(data)
        alert(status)
      })
      e.preventDefault()
    });
  });

  console.log("HOWDY")