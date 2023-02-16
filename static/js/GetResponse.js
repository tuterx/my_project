$(document).ready(function() {
  // 绑定 Send 按钮的点击事件
  $('#getresponse').click(function() {
    // 获取问题内容
    var question = $('input[name=question]').val();
    // 发送 AJAX 请求
    $.ajax({
      type: 'POST',
      url: 'chatbot/get_response',
      data: {question: question},
      success: function(data) {
        // 更新页面上的结果区域
        $('#chatlog textarea').val(data);
      }
    });
  });
});
