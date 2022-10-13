import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http'; 
import { Message } from '../models/ia/Message';

@Injectable({
  providedIn: 'root'
})
export class IaService {

  constructor(private http: HttpClient) { }

  url = "http://localhost:8000/consultas/"

  public sendMessage(message: Message): Observable<Message>{
    return this.http.post<Message>(this.url, message);
  }
}
