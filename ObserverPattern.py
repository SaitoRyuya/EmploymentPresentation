#!/usr/bin/python3
# -*- coding:utf-8 -*-

class Observer:
    def __init__(self):
        pass

    def update(self, model):
        pass


class Observable:
    def __init__(self):
        self.__observers = set()

    def clear(self):
        self.__observers = set()

    def removeObserver(self, observer_id):
        self.__observers.remove(observer_id)

    def addObserver(self, observer):
        self.__observers.add(observer)

    def notifyObservers(self):
        for observer in self.__observers:
            observer.update(self)
