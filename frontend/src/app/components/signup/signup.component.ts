import {
  HttpClient,
  HttpErrorResponse,
  HttpEventType,
  HttpParams,
  HttpResponse,
} from '@angular/common/http';
import { Component, ErrorHandler, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss'],
})
export class SignupComponent implements OnInit {
  userForm = new FormGroup({
    name: new FormControl(''),
    email: new FormControl(''),
    password: new FormControl(''),
  });
  errorMessage: string = '';
  successMessage: string = '';
  isAccountCreated: boolean = false;
  constructor(private httpClient: HttpClient) {}

  ngOnInit(): void {}

  public onSubmit() {
    const username = this.userForm.get('name')?.value;
    const email = this.userForm.get('email')?.value;
    const password = this.userForm.get('password')?.value;
    let param = new HttpParams();
    param = param.append('name', username);
    param = param.append('email', email);
    param = param.append('password', password);
    this.httpClient
      .request('post', 'http://127.0.0.1:8000/signup/', { params: param })
      ?.subscribe(
        (_res) => {
          this.isAccountCreated = true;
          console.log(_res);
        },
        (_error: HttpErrorResponse) => {
          this.isAccountCreated = false;

          this.errorMessage = 'My username or email is Already Exists! , May Email is Invalid';
        }
      );
  }
}
