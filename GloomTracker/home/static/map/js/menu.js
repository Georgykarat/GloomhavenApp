$(function(){ 

    var PlusRep = $('#plusrep');
    var MinRep = $('#minrep');
    var PlusPro = $('#pluspro');
    var MinPro = $('#minpro');
    var Pro = $('#pro');
    var Rep = $('.repbtn');
    var PlusCh = $('#plusch');
    var MinCh = $('#minch');
    var ProCh = $('#ch');
    var ProsperityLevel = $('#pros-level');
    var DiscountLevel = $('#disc-level');
    // var ChooseSquadZone = $('.main-choose-squad-bstrip');
    // var NewSquadForm = $('.main-choose-squad-bform');
    // var SquadNameNew = $('#squadname-in');
    // var SquadDescNew = $('#squaddesc-in');
    // var SquadGoBtn = $('.main-go-squad-btn');
    // var Squad = $('.main-count-zone-stroke');


    // NewSquadBtn.on('click', function(){
    //     if (NewSquadBtn.text() != 'Назад') {
    //         ChooseSquadZone.css('display', 'none');
    //         NewSquadForm.css('display', 'flex');
    //         NewSquadBtn.text('Назад');
    //     } else {
    //         ChooseSquadZone.css('display', 'flex');
    //         NewSquadForm.css('display', 'none');
    //         NewSquadBtn.text('Создать отряд');
    //         SquadNameNew.val('');
    //         SquadDescNew.val('');
    //     }
    // });

    PlusRep.on('click', function(){
            let rep = Rep.text()
            $.ajax({
                type: 'GET',
                url: 'addrep/',
                data: {

                },
                success: function(response) {
                    responsecode = response.responsecode;
                    result = response.result;
                    discount = response.disc;
                    Rep.text(result);
                    DiscountLevel.text(discount);
                    if (discount <= -1) {
                        DiscountLevel.css('color', 'green');
                    } else if (discount >= 1) {
                        DiscountLevel.css('color', 'red');
                    } else {
                        DiscountLevel.css('color', 'white');
                    }
                }
            });
    });

    MinRep.on('click', function(){
        let rep = Rep.text()
        $.ajax({
            type: 'GET',
            url: 'minrep/',
            data: {

            },
            success: function(response) {
                responsecode = response.responsecode;
                result = response.result;
                discount = response.disc;
                Rep.text(result);
                DiscountLevel.text(discount);
                    if (discount <= -1) {
                        DiscountLevel.css('color', 'green');
                    } else if (discount >= 1) {
                        DiscountLevel.css('color', 'red');
                    } else {
                        DiscountLevel.css('color', 'white');
                    }
            }
        });
    });

        PlusPro.on('click', function(){
            $.ajax({
                type: 'GET',
                url: 'addpro/',
                data: {

                },
                success: function(response) {
                    responsecode = response.responsecode;
                    result = response.result;
                    level = response.level;
                    Pro.text(result);
                    ProsperityLevel.text(level);    
                }
            });
        });

    MinPro.on('click', function(){
        $.ajax({
            type: 'GET',
            url: 'minpro/',
            data: {

            },
            success: function(response) {
                responsecode = response.responsecode;
                result = response.result;
                level = response.level;
                Pro.text(result);
                ProsperityLevel.text(level);
            }
        });
});

PlusCh.on('click', function(){
    $.ajax({
        type: 'GET',
        url: 'addch/',
        data: {

        },
        success: function(response) {
            responsecode = response.responsecode;
            result = response.result;
            ProCh.text(result);
            
        }
    });
});

MinCh.on('click', function(){
$.ajax({
    type: 'GET',
    url: 'minch/',
    data: {

    },
    success: function(response) {
        responsecode = response.responsecode;
        result = response.result;
        ProCh.text(result)
    }
});
});

    // Squad.on('click', function(){
    //     Squad.css('border-top', '1px solid black');
    //     Squad.css('border-bottom', '1px solid black');
    //     Squad.css('background-color', '#000000AA');
    //     $(this).css('border-top', '1px solid gold');
    //     $(this).css('border-bottom', '1px solid gold');
    //     $(this).css('background-color', '#936b09');
    // })
});