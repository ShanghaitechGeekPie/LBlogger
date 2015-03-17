$(function(){
	$.backstretch([
		"/static/image/bg.jpg"
	], {
		fade: 1000,
		duration: 7000
	});	


	$(function () {
		$('[data-toggle="popover"]').popover()
	})
	var date=new Date();
	$(".form_datetime").val(date.getFullYear()+'-'+(date.getMonth()+1)+'-'+date.getDate()+' '+date.getHours()+':'+date.getMinutes());
	$(".form_datetime").datetimepicker({format: 'yyyy-mm-dd hh:ii',todayHighlight:true,todayBtn:true,autoclose:true});
	var editor = new Simditor({
		textarea: $('#editor'),
		toolbarFloat: true,
		toolbarFloatOffset: 53
	});
}) 
