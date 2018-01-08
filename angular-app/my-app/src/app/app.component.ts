import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';

  stream = {
    source: 'http://192.168.0.108:81/dash/test.mpd',
  };
}
