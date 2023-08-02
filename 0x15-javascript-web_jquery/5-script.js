// add a new <li> element to the list <ul class="my_list"> OnClick on the <div id="add_item">.
$(document).ready(function () {
    $('#add_item').click(function () {
      var newLiElement = $('<li>Item</li>');
  
      // Append the new <li> element to the UL.my_list
      $('ul.my_list').append(newLiElement);
    });
  });