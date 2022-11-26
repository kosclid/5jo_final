from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name="dispatch")
def movetotext(request):
    return render(
        request,
        "translang/movetotext.html",
        {},
    )


from django.http import JsonResponse
import json
import numpy as np
from tensorflow.keras.models import load_model

seq = []
action_seq = []


@method_decorator(csrf_exempt, name="dispatch")
def home(request):
    context = 0
    seq_length = 30
    this_action = "?"

    actions = [
        "no",
        "dont",
        "sorry",
        "thank",
        "go",
        "do",
        "joy",
        "gjoy",
        "sua",
        "tired",
    ]

    model = load_model("models/model.h5")

    if request.method == "POST":
        this_action = "????"
        data = json.loads(request.body)
        # do something
        # print(data)
        data = data[0]

        rh0 = data[0]
        rh1 = data[1]
        rh2 = data[2]
        rh3 = data[3]
        rh4 = data[4]
        rh5 = data[5]
        rh6 = data[6]
        rh7 = data[7]
        rh8 = data[8]
        rh9 = data[9]
        rh10 = data[10]
        rh11 = data[11]
        rh12 = data[12]
        rh13 = data[13]
        rh14 = data[14]
        rh15 = data[15]
        rh16 = data[16]
        rh17 = data[17]
        rh18 = data[18]
        rh19 = data[19]
        rh20 = data[20]

        vrh01 = np.array(
            [rh1["x"] - rh0["x"], rh1["y"] - rh0["y"], rh1["z"] - rh0["z"]]
        )
        vrh12 = np.array(
            [rh2["x"] - rh1["x"], rh2["y"] - rh1["y"], rh2["z"] - rh1["z"]]
        )
        vrh23 = np.array(
            [rh3["x"] - rh2["x"], rh3["y"] - rh2["y"], rh3["z"] - rh2["z"]]
        )
        vrh34 = np.array(
            [rh4["x"] - rh3["x"], rh4["y"] - rh3["y"], rh4["z"] - rh3["z"]]
        )
        vrh05 = np.array(
            [rh5["x"] - rh0["x"], rh5["y"] - rh0["y"], rh5["z"] - rh0["z"]]
        )
        vrh56 = np.array(
            [rh6["x"] - rh5["x"], rh6["y"] - rh5["y"], rh6["z"] - rh5["z"]]
        )
        vrh67 = np.array(
            [rh7["x"] - rh6["x"], rh7["y"] - rh6["y"], rh7["z"] - rh6["z"]]
        )
        vrh78 = np.array(
            [rh8["x"] - rh7["x"], rh8["y"] - rh7["y"], rh8["z"] - rh7["z"]]
        )
        vrh59 = np.array(
            [rh9["x"] - rh5["x"], rh9["y"] - rh5["y"], rh9["z"] - rh5["z"]]
        )
        vrh910 = np.array(
            [rh10["x"] - rh9["x"], rh10["y"] - rh9["y"], rh10["z"] - rh9["z"]]
        )
        vrh1011 = np.array(
            [rh11["x"] - rh10["x"], rh11["y"] - rh10["y"], rh11["z"] - rh10["z"]]
        )
        vrh1112 = np.array(
            [rh12["x"] - rh11["x"], rh12["y"] - rh11["y"], rh12["z"] - rh11["z"]]
        )
        vrh913 = np.array(
            [rh13["x"] - rh9["x"], rh13["y"] - rh9["y"], rh13["z"] - rh9["z"]]
        )
        vrh1314 = np.array(
            [rh14["x"] - rh13["x"], rh14["y"] - rh13["y"], rh14["z"] - rh13["z"]]
        )
        vrh1415 = np.array(
            [rh15["x"] - rh14["x"], rh15["y"] - rh14["y"], rh15["z"] - rh14["z"]]
        )
        vrh1516 = np.array(
            [rh16["x"] - rh15["x"], rh16["y"] - rh15["y"], rh16["z"] - rh15["z"]]
        )
        vrh1317 = np.array(
            [rh17["x"] - rh13["x"], rh17["y"] - rh13["y"], rh17["z"] - rh13["z"]]
        )
        vrh017 = np.array(
            [rh17["x"] - rh0["x"], rh17["y"] - rh0["y"], rh17["z"] - rh0["z"]]
        )
        vrh1718 = np.array(
            [rh18["x"] - rh17["x"], rh18["y"] - rh17["y"], rh18["z"] - rh17["z"]]
        )
        vrh1819 = np.array(
            [rh19["x"] - rh18["x"], rh19["y"] - rh18["y"], rh19["z"] - rh18["z"]]
        )
        vrh1920 = np.array(
            [rh20["x"] - rh19["x"], rh20["y"] - rh19["y"], rh20["z"] - rh19["z"]]
        )

        uvrh01 = vrh01 / np.linalg.norm(vrh01)
        uvrh12 = vrh12 / np.linalg.norm(vrh12)
        uvrh23 = vrh23 / np.linalg.norm(vrh23)
        uvrh34 = vrh34 / np.linalg.norm(vrh34)
        uvrh05 = vrh05 / np.linalg.norm(vrh05)
        uvrh56 = vrh56 / np.linalg.norm(vrh56)
        uvrh67 = vrh67 / np.linalg.norm(vrh67)
        uvrh78 = vrh78 / np.linalg.norm(vrh78)
        uvrh59 = vrh59 / np.linalg.norm(vrh59)
        uvrh910 = vrh910 / np.linalg.norm(vrh910)
        uvrh1011 = vrh1011 / np.linalg.norm(vrh1011)
        uvrh1112 = vrh1112 / np.linalg.norm(vrh1112)
        uvrh913 = vrh913 / np.linalg.norm(vrh913)
        uvrh1314 = vrh1314 / np.linalg.norm(vrh1314)
        uvrh1415 = vrh1415 / np.linalg.norm(vrh1415)
        uvrh1516 = vrh1516 / np.linalg.norm(vrh1516)
        uvrh1317 = vrh1317 / np.linalg.norm(vrh1317)
        uvrh017 = vrh017 / np.linalg.norm(vrh017)
        uvrh1718 = vrh1718 / np.linalg.norm(vrh1718)
        uvrh1819 = vrh1819 / np.linalg.norm(vrh1819)
        uvrh1920 = vrh1920 / np.linalg.norm(vrh1920)

        d = np.concatenate(
            (
                uvrh01,
                uvrh12,
                uvrh23,
                uvrh34,
                uvrh05,
                uvrh56,
                uvrh67,
                uvrh78,
                uvrh59,
                uvrh910,
                uvrh1011,
                uvrh1112,
                uvrh913,
                uvrh1314,
                uvrh1415,
                uvrh1516,
                uvrh1317,
                uvrh017,
                uvrh1718,
                uvrh1819,
                uvrh1920,
            ),
            axis=None,
        )

        seq.append(d)

        if len(seq) >= seq_length:

            input_data = np.expand_dims(
                np.array(seq[-seq_length:], dtype=np.float32), axis=0
            )

            y_pred = model.predict(input_data).squeeze()
            i_pred = int(np.argmax(y_pred))

            conf = y_pred[i_pred]

            if conf >= 0.9:

                action = actions[i_pred]
                action_seq.append(action)

                if len(action_seq) >= 3:

                    if action_seq[-1] == action_seq[-2] == action_seq[-3]:
                        this_action = action
                        print(this_action)

    context = {
        "result": this_action,
    }
    return JsonResponse(context)


