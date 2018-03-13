import type {DraggableId, DraggableLocation} from "react-beautiful-dnd/lib/types";

export type Task = {|
  fields: {
    assigned: boolean,
    board: number,
    column: number,
    description: string,
    title: string,
    userID: number,
    members: string[],
    colour : string,
    index: number,
  },
  model: string,
  pk: number,
|}

export type Column = {|
  fields: {
    board: number,
    description: string,
    title: string,
  },
  model: string,
  pk: number,
|}

export type Column = {|
  fields: {
    board: number,
    description: string,
    title: string,
  },
  model: string,
  pk: number,
|}



export type TaskMap = {
  [key: string]: Task[]
}

export type UserMap = [
  [{key: string}]
]

export type Dragging = {|
  id: DraggableId,
  location: DraggableLocation,
|}


export type TaskUpdate = {|
  task: Task,
  title: string,
  desc: string,
  members: [{value : string}],
  colour: string
|}