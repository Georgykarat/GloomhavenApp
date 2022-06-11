$(function(){ 

    var NewSquadBtn = $('.main-create-squad-btn');
    var ChooseSquadZone = $('.main-choose-squad-bstrip');
    var NewSquadForm = $('.main-choose-squad-bform');
    var SquadNameNew = $('#squadname-in');
    var SquadDescNew = $('#squaddesc-in');
    var SquadGoBtn = $('.main-go-squad-btn');
    var Squad = $('.main-count-zone-stroke');


    NewSquadBtn.on('click', function(){
        if (NewSquadBtn.text() != 'Назад') {
            ChooseSquadZone.css('display', 'none');
            NewSquadForm.css('display', 'flex');
            NewSquadBtn.text('Назад');
        } else {
            ChooseSquadZone.css('display', 'flex');
            NewSquadForm.css('display', 'none');
            NewSquadBtn.text('Создать отряд');
            SquadNameNew.val('');
            SquadDescNew.val('');
        }
    });

    SquadGoBtn.on('click', function(){
        if (SquadNameNew.val() != '' & SquadDescNew.val() != '') {
            let squadname = SquadNameNew.val();
            let squaddesc = SquadDescNew.val();
            $.ajax({
                type: 'GET',
                url: 'createsquad/',
                data: {
                    squadname: squadname,
                    squaddesc: squaddesc,
                },
                success: function(response) {
                    responsecode = response.responsecode;
                }
            });
        } 
    })

    Squad.on('click', function(){
        Squad.css('border-top', '1px solid black');
        Squad.css('border-bottom', '1px solid black');
        Squad.css('background-color', '#000000AA');
        $(this).css('border-top', '1px solid gold');
        $(this).css('border-bottom', '1px solid gold');
        $(this).css('background-color', '#936b09');
    })
});