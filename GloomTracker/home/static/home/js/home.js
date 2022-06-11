$(function(){ 

    var NewSquadBtn = $('.main-create-squad-btn');
    var ChooseSquadZone = $('.main-choose-squad-bstrip');


    NewSquadBtn.on('click', function(){
        if (NewSquadBtn.text() != 'Назад') {
            ChooseSquadZone.css('display', 'none');
            NewSquadBtn.text('Назад');
        } else {
            ChooseSquadZone.css('display', 'flex');
            NewSquadBtn.text('Создать отряд');
        }
    });
});