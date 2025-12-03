using Toybox.Application as App;
using Toybox.Lang as Lang;

class Storage {

    const KEY_CHECKINS = "checkins";

    // Save a check-in entry to persistent storage.
    // This is a simple append-only list stored as an app property.
    static function saveCheckIn(data as Lang.Dictionary) {
        var app = App.getApp();
        var existing = app.getProperty(KEY_CHECKINS);

        if (existing == null) {
            existing = [];
        }

        existing.add(data);
        app.setProperty(KEY_CHECKINS, existing);
    }

}
