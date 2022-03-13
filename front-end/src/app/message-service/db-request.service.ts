import { Injectable } from '@angular/core';
import {Table} from "../table";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class DbRequestService {
  table: Table = {
    id: 1,
    name: "MyTable1"
  };

  private flaskHttp = "http://127.0.0.1:5000/tables"

  constructor(private http: HttpClient) { }

  getTables() : Observable<Table[]> {
    return this.http.get<Table[]>(this.flaskHttp)
  }
}
