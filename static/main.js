$(function() {
  console.log( "ready!" );
  $('.delete-item').on('click', function(){
    console.log("test")
    var entry = $(this).parent().get(0);
    console.log(entry);
    var entry = $(this).parent();
    console.log(entry);

    var post_id = $(this).parent().find('h2').attr('id');
    console.log("the post id is : "+post_id);
    console.log(post_id);
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

$(function() {
  console.log( "ready!" );
  $('.get-download-link').on('click', function(){
    console.log("test")
    var post_id = $(this).parent().find('h2').attr('id');
    console.log("the post id is : "+post_id);
    var entry = $(this).parent();
    console.log(entry);

    $.ajax({
      type:'GET',
      url: '/gettempurl' + '/' + post_id,
      context: entry,
      success:function(result){
        if(result['status'] === 1){
          console.log(result['url']);
          $('#temp-url').html('<div class="alert alert-info alert-dismissible">'+'The temporaray URL : <strong><a href="'+result['url']+'">'+  result['url'] +'</a></strong><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">×</span></button> </div>')                  
}
      }
    });
  });
});
 

