$('document').ready(function(){
var current = 0;
var score = 0;
var question = $('.question');
var dys = "";
question.hide();
$('#but').hide();
$('#Score').hide();
$("button[name='start']").click(function () {
  $('#First').hide();
  $(question[current]).show();
  $('#but').show();
});
$('#submit').hide();
$('#prev').attr('disabled',true);

$("#next").click(function(){
  $(question[current]).hide();
  current++;
  $(question[current]).show();
  if(current===9){
      $('#next').attr('disabled',true);
      $('#submit').show();}
  $('#prev').attr('disabled',false);
});
$("#prev").click(function(){
  $(question[current]).hide();
  current--;
  $(question[current]).show();
  if(current===0){
    $('#prev').attr('disabled',true);
  }
  $('#next').attr('disabled',false);
  $('#submit').hide();
});
$("#submit").click(function(){
  question.hide();
  for(var i=0;i<10;i++){
    if(parseInt($(question[i]).find('input[name="options"]:checked').val())===1)
      score++;
  }
  if(score <= 3)
	dys = "Thanks for your patience,No need to worry.Your ward is not Dyslexic";	
  else if(score <= 6)
	dys = "Your ward is mildly Dyslexic,Its time to take all the symptoms seriously and pay a close attention";
  else if(score > 6)
	dys = "Your ward is Dyslexic, please pay special attention";
  //alert(dys);
  $('#score').text(dys);
  $("#Score").show();
  $('#but').hide();
});
$('#restart').click(function(){
  location.reload();
});

});