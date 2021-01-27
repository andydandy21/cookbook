$(function() {
    $("#add").click(function(){

        var formsetWrapper = $("<div class=\"formsetwrapper\" id=\"field\"/>");
        var fieldOne = $("<input type=\"text\" placeholder=\"quantity\">");
        var fieldTwo = $("<select style=\"margin-right: 4px;\"><option>Unit</option><option>Oz</option><option>Grams</option></select>");
        var fieldThree = $("<input type=\"text\" placeholder=\"ingredient\">");
        var removeButton = $("<input type=\"button\" class=\"remove\" value=\"-\"/>");
        removeButton.click(function(){
            $(this).parent().remove();
        });
        formsetWrapper.append(fieldOne);
        formsetWrapper.append(fieldTwo);
        formsetWrapper.append(fieldThree);
        formsetWrapper.append(removeButton);
        $("#recipe-formset").append(formsetWrapper);
    });
});
