using Toybox.WatchUi as Ui;
using Toybox.System as Sys;
using Toybox.Lang as Lang;

class CheckInView extends Ui.View {

    var _dizziness = 0;
    var _vertigo = 0;
    var _hotFlash = 0;

    function initialize() {
        Ui.View.initialize();
        setLayout(Rez.Layouts.CheckInLayout);
    }

    function onShow() {
        // Vibrate when the view appears
        Sys.vibrate(Sys.VIBE_SHORT);
    }

    function onUpdate(dc as Ui.Drawable) {
        // No custom drawing needed, layout handles UI
    }

    function onHide() {
        // Called when the view is hidden
    }

    function onControl(event as Ui.ControlEvent) {
        var id = event.getControlId();

        if (id == :dizzinessPicker) {
            _dizziness = event.getValue();

        } else if (id == :vertigoPicker) {
            _vertigo = event.getValue();

        } else if (id == :hotFlashPicker) {
            _hotFlash = event.getValue();

        } else if (id == :saveButton) {
            saveAndExit();
        }
    }

    function saveAndExit() {

        var data = {
            :timestamp => Sys.getClockTime(),
            :dizziness => _dizziness,
            :vertigo => _vertigo,
            :hot_flash_intensity => _hotFlash
        };

        Storage.saveCheckIn(data);

        Sys.vibrate(Sys.VIBE_SHORT);
        Ui.popView();
    }

}
