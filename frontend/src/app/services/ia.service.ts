import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http'; 
import { Message } from '../models/ia/Message';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':  'application/json',
    'Authorization': 'Basic ' + btoa('uciel:1234')
  })
};

@Injectable({
  providedIn: 'root'
})
export class IaService {

  constructor(private http: HttpClient) { }

  //url =  "http://localhost:5000/query_ia"

  url = "http://localhost:8000/consultas/"

  /*public getMessage(menssage: Message): Observable<Message[]>{
    return this.http.get<Message[]>(this.url + `?str_query=${menssage.response}`);
  }*/

  /*public sendMessage(message: Message): Observable<Message>{
    return this.http.post<Message>(this.url + `?str_query=${message.message}`, message);
  }*/

  public sendMessage(message: Message): Observable<Message>{
    return this.http.post<Message>(this.url, message, httpOptions);
  }
}
