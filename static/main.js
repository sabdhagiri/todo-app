$(function() {
  console.log( "ready!" );
  $('.entry').on('click', function(){
    console.log("clicked on post")
    var entry = this;
    var post_id = $(this).find('h2').attr('id');
    console.log("The post id is "+post_id)
    $.ajax({
      type:'GET',
      url: '/delete' + '/' + post_id,
      context: entry,
      success:function(result){
        if(result['status'] === 1){
          $(this).remove();
          console.log(result);
        }
      }
    });
  });
});

