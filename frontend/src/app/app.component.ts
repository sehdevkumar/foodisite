import { Component } from '@angular/core';
import { Route, Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  constructor(private route: Router) {}
  menuList = ['Home', 'Add Post', 'Login', 'Signup', 'About', 'Contact Us'];

  public onRouteChange(route: string) {
    this.route.navigateByUrl(route.toLowerCase().replace(' ', ''));
  }
}
