using Toybox.Application as App;
using Toybox.WatchUi as Ui;

class HormoneCheckInApp extends App.AppBase {

    function initialize() {
        App.AppBase.initialize();
    }

    function onStart(state) {
        // Push the main view when the app starts
        Ui.pushView(new CheckInView(), Ui.SLIDE_IMMEDIATE);
    }

    function onStop(state) {
        // Cleanup if necessary
    }

    function onBackground() {
        // App moved to background
    }

    function onResume(state) {
        // App returned to foreground
    }
}
