var categories_tag=''
for(let i=0;i<categories.length;i++)
{
  categories_tag+='<div class="category">'+categories[i][0]+'</div>'
}

$(document).ready(function(){
  $('.categories').append(categories_tag)
})



var item=''
for(let i=0;i<items.length;i++)
{
    item+='<tr><td><img src="../static/images/'+items[i][4]+'" class="img-thumbnail" /></td>'
    item+='<td><p><b>'+items[i][1].toUpperCase()+'</b></p><p>'+items[i][2]+'</p><p>Amount : <span class="'+items[i][1]+'">'+items[i][3]+'</span>/KG</p></td>'
    item+='<td class="authenticate"><input type="number" min="0" class="form-control '+items[i][1]+'" /><button class="btn btn-primary" type="button" name="'+items[i][1]+'">Add</button></td>'

}

$(document).ready(function(){
    $('.item tbody').append(item)
    $('.authenticate').hide();
    $('.item').css("width", "50%")
})


var total_amount = 0;
var object = []

$(document).ready(function(){
  $('.authenticate button').click(function(){
    var classname = $(this).attr('name')
    var item = $("."+classname)
    var quantity = parseInt($("."+classname).get(1).value);
    var amount = quantity * parseInt($("."+classname).get(0).innerHTML)
    if(isNaN(quantity) || quantity<1){
      alert('Enter valid quantity');
    }
    else{
      total_amount += amount;
      var tags = '';
      tags+='<tr><td>'+classname+'</td><td>'+quantity+'</td><td>'+amount+'</td></tr>'
      $('#orders').append(tags);
      $('#submit').html('Checkout : '+total_amount) 
      let arr = {classname, quantity, amount}
      
      object.push(arr);
      console.log(object)
    }
  })
})


$(document).ready( function() {
    $('#submit').click(function() {
      const jsonString = JSON.stringify(Object.assign({}, object))
      $.ajax({
        type: 'POST',
        contentType: 'application/json',
        data: jsonString,
        dataType: 'json',
        url: 'http://127.0.0.1:5000/home',
        success: function (e) {
            alert("Order placed successfully")
            location.reload();
            
        },
        error: function(error) {
          alert("Order placed successfully")
          location.reload();
        }
    });
    });
  });

$(document).ready(function(){
  $('.search-option input').on("keyup", function(){
    var value = $('.search-option input').val().toLowerCase()
    $('.item tr').filter(function(){
      $(this).toggle($(this).text().toLowerCase().indexOf(value)>-1)
    })
  })
})

$(document).ready(function(){
  $('.category').on("click", function(){
    var value = $(this).text().toLowerCase()
    $('.item tr').filter(function(){
      $(this).toggle($(this).text().toLowerCase().indexOf(value)>-1)
    })
  })
})
