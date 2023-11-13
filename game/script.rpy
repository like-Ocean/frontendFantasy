label start:
    scene bg_room

    Andrew "Так, завтра мне надо произвести фурор на собеседовании."
    Andrew "Как мне это сделать, если у меня нет нормальной одежды. Как повезло богатым людям."
    Andrew "Мааам!"

    show Mom at right
    Mom "Что сынок?"
    Andrew "Я не могу выбрать одежду, помоги."
    Mom "А чем тебе не нравится костюм, который мы покупали на выпускной?"
    Andrew "Ну мам, это уже не выпускной."

    Mom "Ну ладно, сейчас принесу другой"
    hide Mom
    play sound door_sound fadein(0.2)
    pause 2.0
    show Mom at right

    Mom "Может это подойдет?"
    menu:
        "У тебя нет никакого вкуса!":
            Andrew "У тебя нет никакого вкуса!"
            Mom "..."
            hide Mom
        "Спасибо мам, он очень красивый.":
            Andrew "Спасибо мам, он очень красивый."
            Mom "Рада помочь!"
            play sound door_sound
            hide Mom

    pause 0.5
    # Андрей ложится на кровать
    scene bg_room with dissolve
    hide Mom

    # Андрей засыпает
    Andrew "(Пока посмотрю видео про frontend разработчика.)"
    pause 2.0
    Andrew "(Зевает) Аааа, какая скучная тема. Лучше бы я поспал."
    pause 1.0

    scene black
    pause 3.0

    scene bg_street with fade

    Andrew "Стоп, что я делаю на улице в домашней одежде."
    # Андрей видит свой шкаф
    Andrew "Оооо, повезло!"
    # Андрей заходит в шкаф
    show closet at right with dissolve
    Andrew "Надо быстро выбрать одежду, а то автобус скоро приедет."
    play sound door_sound
    menu:
        "Спортивный Костюм":
            $ outfit = "sport"
            Andrew "Надену спортивный костюм, покажусь спортивным."
        "Отцовский свадебный костюм":
            $ outfit = "wedding"
            Andrew "Надену отцовский свадебный костюм, покажусь элегантным."
        "Костюм с выпускного":
            $ outfit = "graduation"
            Andrew "Надену костюм с выпускного, покажусь серьезным."
        "Джинсы и футболка":
            $ outfit = "casual"
            Andrew "Надену джинсы и футболку, покажусь кежуал."

    Andrew "Ну всё, теперь можно ехать!"
    # Андрей подходит к прохожему
    show Stranger at right
    hide closet with dissolve

    Andrew "Простите, можете пожалуйста подсказать где автобус."
    Stranger "А вы не хотите добраться быстрее?"
    Andrew "Хочу, а как?"

    show portal at left
    play sound portal_sound
    Stranger "Вот как!"
    Stranger "Называйте координаты места."
    Andrew "620078"
    Stranger "Ок."
    # Андрей заходит в портал
    show portal at left with fade
