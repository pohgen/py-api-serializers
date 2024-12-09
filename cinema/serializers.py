from rest_framework import serializers

from cinema.models import Movie, Genre, Actor, MovieSession, CinemaHall, Order, Ticket


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("title", "description", "duration", "genres", "actors")


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("name",)


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("first_name", "last_name")


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ("show_time", "movie", "cinema_hall")


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("name", "rows", "seats_in_row", "capacity")


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("created_at", "user")


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ("movie_session", "order", "row", "seat")
